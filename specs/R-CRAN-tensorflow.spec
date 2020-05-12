%global packname  tensorflow
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}
Summary:          R Interface to 'TensorFlow'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.2
BuildRequires:    R-CRAN-reticulate >= 1.10
BuildRequires:    R-CRAN-tfruns >= 1.0
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-jsonlite >= 1.2
Requires:         R-CRAN-reticulate >= 1.10
Requires:         R-CRAN-tfruns >= 1.0
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-config 
Requires:         R-CRAN-processx 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
Interface to 'TensorFlow' <https://www.tensorflow.org/>, an open source
software library for numerical computation using data flow graphs. Nodes
in the graph represent mathematical operations, while the graph edges
represent the multidimensional data arrays (tensors) communicated between
them. The flexible architecture allows you to deploy computation to one or
more 'CPUs' or 'GPUs' in a desktop, server, or mobile device with a single
'API'. 'TensorFlow' was originally developed by researchers and engineers
working on the Google Brain Team within Google's Machine Intelligence
research organization for the purposes of conducting machine learning and
deep neural networks research, but the system is general enough to be
applicable in a wide variety of other domains as well.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
