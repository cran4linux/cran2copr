%global packname  tcl
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Testing in Conditional Likelihood Context

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-eRm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-splines 
BuildRequires:    R-Matrix 
BuildRequires:    R-lattice 
Requires:         R-CRAN-eRm 
Requires:         R-CRAN-numDeriv 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-splines 
Requires:         R-Matrix 
Requires:         R-lattice 

%description
An implementation of extended Rasch modeling hypothesis testing in R.
Provides 4 statistical tests, i.e. gradient test (GR), likelihood ratio
test (LR), Rao score or Lagrange multiplier test (RS), and Wald test, for
testing a number of hypotheses referring to the Rasch model (RM), linear
logistic test model (LLTM), rating scale model (RSM), and partial credit
model (PCM).

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
