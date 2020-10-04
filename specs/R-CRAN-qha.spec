%global packname  qha
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          3%{?dist}%{?buildtag}
Summary:          Qualitative Harmonic Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-FactoClass 
BuildRequires:    R-CRAN-FactoMineR 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-FactoClass 
Requires:         R-CRAN-FactoMineR 

%description
Multivariate description of the state changes of a qualitative variable by
Correspondence Analysis and Clustering. See: Deville, J.C., & Saporta, G.
(1983). Correspondence analysis, with an extension towards nominal time
series. Journal of econometrics, 22(1-2), 169-189. Corrales, M.L., &
Pardo, C.E. (2015) <doi:10.15332/s2027-3355.2015.0001.01>. Analisis de
datos longitudinales cualitativos con analisis de correspondencias y
clasificacion. Comunicaciones en Estadistica, 8(1), 11-32.

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
