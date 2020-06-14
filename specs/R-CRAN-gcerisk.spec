%global packname  gcerisk
%global packver   19.05.24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          19.05.24
Release:          2%{?dist}
Summary:          Generalized Competing Event Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-cmprsk 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-survival 
Requires:         R-CRAN-cmprsk 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
Generalized competing event model based on Cox PH model and Fine-Gray
model. This function is designed to develop optimized risk-stratification
methods for competing risks data, such as described in: 1. Carmona R,
Gulaya S, Murphy JD, Rose BS, Wu J, Noticewala S,McHale MT, Yashar CM,
Vaida F, and Mell LK (2014) <DOI:10.1016/j.ijrobp.2014.03.047>. 2. Carmona
R, Zakeri K, Green G, Hwang L, Gulaya S, Xu B, Verma R, Williamson CW,
Triplett DP, Rose BS, Shen H, Vaida F, Murphy JD, and Mell LK (2016)
<DOI:10.1200/JCO.2015.65.0739>. 3. Lunn, Mary, and Don McNeil (1995)
<DOI:10.2307/2532940>.

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
