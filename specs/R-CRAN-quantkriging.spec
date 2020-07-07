%global packname  quantkriging
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Quantile Kriging for Stochastic Simulations with Replication

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-Matrix >= 1.2.17
BuildRequires:    R-CRAN-hetGP >= 1.1.1
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-Matrix >= 1.2.17
Requires:         R-CRAN-hetGP >= 1.1.1
Requires:         R-stats 

%description
A re-implementation of quantile kriging. Quantile kriging was described by
Plumlee and Tuo (2014) <doi:10.1080/00401706.2013.860919>.  With
computational savings when dealing with replication from the recent paper
by Binois, Gramacy, and Ludovski (2018)
<doi:10.1080/10618600.2018.1458625> it is now possible to apply quantile
kriging to a wider class of problems.  In addition to fitting the model,
other useful tools are provided such as the ability to automatically
perform leave-one-out cross validation.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
