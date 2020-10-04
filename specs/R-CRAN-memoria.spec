%global packname  memoria
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Quantifying Ecological Memory in Palaeoecological Datasets andOther Long Time-Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-HH 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-HH 
Requires:         R-CRAN-tidyr 

%description
Tools to quantify ecological memory in long time-series with Random Forest
models (Breiman 2001 <doi:10.1023/A:1010933404324>) fitted with the
'ranger' library (Wright and Ziegler 2017 <doi:10.18637/jss.v077.i01>).
Particularly oriented to palaeoecological datasets and simulated pollen
curves produced by the 'virtualPollen' package, but also applicable to
other long time-series involving a set of environmental drivers and a
biotic response.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
