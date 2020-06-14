%global packname  MWright
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          2%{?dist}
Summary:          Mainardi-Wright Family of Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cubature 
Requires:         R-stats 
Requires:         R-CRAN-cubature 

%description
Implements random number generation, plotting, and estimation algorithms
for the two-parameter one-sided and two-sided M-Wright (Mainardi-Wright)
family. The M-Wright distributions naturally generalize the widely used
one-sided (Airy and half-normal or half-Gaussian) and symmetric (Airy and
Gaussian or normal) models. These are widely studied in time-fractional
differential equations. References: Cahoy and Minkabo (2017)
<doi:10.3233/MAS-170388>; Cahoy (2012) <doi:10.1007/s00180-011-0269-x>;
Cahoy (2012) <doi:10.1080/03610926.2010.543299>; Cahoy (2011); Mainardi,
Mura, and Pagnini (2010) <doi:10.1155/2010/104505>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
