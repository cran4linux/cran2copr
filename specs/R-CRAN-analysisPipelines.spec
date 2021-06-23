%global __brp_check_rpaths %{nil}
%global packname  analysisPipelines
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Compose Interoperable Analysis Pipelines & Put Them inProduction

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pipeR 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-proto 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pipeR 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-proto 
Requires:         R-CRAN-purrr 

%description
Enables data scientists to compose pipelines of analysis which consist of
data manipulation, exploratory analysis & reporting, as well as modeling
steps. Data scientists can use tools of their choice through an R
interface, and compose interoperable pipelines between R, Spark, and
Python. Credits to Mu Sigma for supporting the development of the package.
Note - To enable pipelines involving Spark tasks, the package uses the
'SparkR' package. The SparkR package needs to be installed to use Spark as
an engine within a pipeline. SparkR is distributed natively with Apache
Spark and is not distributed on CRAN. The SparkR version needs to directly
map to the Spark version (hence the native distribution), and care needs
to be taken to ensure that this is configured properly. To install SparkR
from Github, run the following command if you know the Spark version:
'devtools::install_github('apache/spark@v2.x.x', subdir='R/pkg')'. The
other option is to install SparkR by running the following terminal
commands if Spark has already been installed: '$ export
SPARK_HOME=/path/to/spark/directory && cd $SPARK_HOME/R/lib/SparkR/ && R
-e "devtools::install('.')"'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data-icon.png
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/logging.png
%doc %{rlibdir}/%{packname}/output-icon.png
%doc %{rlibdir}/%{packname}/param-icon.png
%doc %{rlibdir}/%{packname}/pipelineViz1.png
%doc %{rlibdir}/%{packname}/pipelineViz2.png
%{rlibdir}/%{packname}/python
%{rlibdir}/%{packname}/python-logo.png
%doc %{rlibdir}/%{packname}/r-logo.png
%doc %{rlibdir}/%{packname}/report.Rmd
%doc %{rlibdir}/%{packname}/report1.png
%doc %{rlibdir}/%{packname}/report2.png
%doc %{rlibdir}/%{packname}/report3.png
%doc %{rlibdir}/%{packname}/spark-logo.png
%doc %{rlibdir}/%{packname}/spark-structured-streaming-logo.png
%doc %{rlibdir}/%{packname}/styles.css
%{rlibdir}/%{packname}/INDEX
