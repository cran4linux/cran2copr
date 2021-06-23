%global __brp_check_rpaths %{nil}
%global packname  cpd
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Complex Pearson Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fAsianOptions 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-fAsianOptions 
Requires:         R-CRAN-Rdpack 

%description
Probability mass function, distribution function, quantile function and
random generation for the Complex Triparametric Pearson (CTP) and Complex
Biparametric Pearson (CBP) distributions developed by Rodriguez-Avi et al
(2003) <doi:10.1007/s00362-002-0134-7>, Rodriguez-Avi et al (2004)
<doi:10.1007/BF02778271> and Olmo-Jimenez et al (2018)
<doi:10.1080/00949655.2018.1482897>. The package also contains
maximum-likelihood fitting functions for these models.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
