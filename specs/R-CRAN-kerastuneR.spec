%global packname  kerastuneR
%global packver   0.1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.2
Release:          2%{?dist}
Summary:          Interface to 'Keras Tuner'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-tidyjson 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-echarts4r 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-keras 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-tidyjson 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-echarts4r 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-keras 

%description
'Keras Tuner' <https://keras-team.github.io/keras-tuner/> is a hypertuning
framework made for humans. It aims at making the life of AI practitioners,
hypertuner algorithm creators and model designers as simple as possible by
providing them with a clean and easy to use API for hypertuning. 'Keras
Tuner' makes moving from a base model to a hypertuned one quick and easy
by only requiring you to change a few lines of code.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
