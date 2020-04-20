%global packname  NSM3
%global packver   1.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.14
Release:          1%{?dist}
Summary:          Functions and Datasets to Accompany Hollander, Wolfe, andChicken - Nonparametric Statistical Methods, Third Edition

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-stats 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-CRAN-ash 
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-CRAN-BSDA 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-fANCOVA 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-km.ci 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-Rfit 
BuildRequires:    R-CRAN-SemiPar 
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-CRAN-waveslim 
Requires:         R-CRAN-combinat 
Requires:         R-MASS 
Requires:         R-CRAN-partitions 
Requires:         R-stats 
Requires:         R-survival 
Requires:         R-CRAN-agricolae 
Requires:         R-CRAN-ash 
Requires:         R-CRAN-binom 
Requires:         R-CRAN-BSDA 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-fANCOVA 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-km.ci 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-np 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-Rfit 
Requires:         R-CRAN-SemiPar 
Requires:         R-CRAN-SuppDists 
Requires:         R-CRAN-waveslim 

%description
Designed to replace the tables which were in the back of the first two
editions of Hollander and Wolfe - Nonparametric Statistical Methods.
Exact procedures are performed when computationally possible.  Monte Carlo
and Asymptotic procedures are performed otherwise.  For those procedures
included in the base packages, our code simply provides a wrapper to
standardize the output with the other procedures in the package.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
