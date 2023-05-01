import os

class Config:
      def __init__(self) -> None:
            # BACK-END
            self.ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
            self.sample_video_path = self.ROOT_DIR + "/data_sample/sample_1.mp4"
            self.db = self.ROOT_DIR + "/db/store_data.db"
            self.region_data_path = self.ROOT_DIR + "/config/store_region.txt"
            self.model_path = self.ROOT_DIR + "/model/ssd_mobilenet_v1_1_metadata_1.tflite"
            
            # FRONT-END
            self.app_width = 1024
            self.app_height = 576
            self.footer_text = """HCI & AI for Industry 4.0  |  MTE - JTEK - USK  |  Genap 2022/2023"""
            self.title_text = """Store Activity Recognition Apps based on RaspberryPi"""
            self.desc_text = """
                                App Description:

                                Aplikasi pengenalan aktivitas pengunjung toko berbasis deep-learning object tracking 
                                yang dibangun pada RaspberryPi OS RaspberryPi 4 Model B.
                                - Keseluran apps dibangun menggunakan bahasa Python 
                                - Sistem back-end dibangun dengan OpenCV dan TFLite.
                                - Sistem front-end dibangun dengan TKinter. 
                              """
            self.help_text = """
                                Contributing Team:
                                                                  
                                Team Supervisor: Dr. Ir. Kahlil, S.T., M.Eng.
                                Back-end Team: M Jurej Alhamdi, Nizam Albar, Jamalur Ridha
                                Front-end Team: Wildan Mumtaz, Teuku Abrar Miftha
                             """