%global __brp_check_rpaths %{nil}
%global packname  bayess
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          2%{?dist}%{?buildtag}
Summary:          Bayesian Essentials with R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-combinat 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-combinat 

%description
bayess contains a collection of functions that allows the reenactment of
the R programs used in the book "Bayesian Essentials with R" (revision of
"Bayesian Core") without further programming. R code being available as
well, they can be modified by the user to conduct one's own simulations.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
