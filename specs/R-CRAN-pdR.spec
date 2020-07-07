%global packname  pdR
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          3%{?dist}
Summary:          Threshold Model and Unit Root Tests in Cross-Section and TimeSeries Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-tcltk 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-coefplot 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-papeR 
Requires:         R-CRAN-plm 
Requires:         R-tcltk 
Requires:         R-boot 
Requires:         R-CRAN-car 
Requires:         R-CRAN-coefplot 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-papeR 

%description
Threshold model, panel version of Hylleberg et al. (1990)
<DOI:10.1016/0304-4076(90)90080-D> seasonal unit root tests, and panel
unit root test of Chang (2002) <DOI:10.1016/S0304-4076(02)00095-7>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
