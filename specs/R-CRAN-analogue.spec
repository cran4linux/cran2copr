%global packname  analogue
%global packver   0.17-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17.5
Release:          1%{?dist}%{?buildtag}
Summary:          Analogue and Weighted Averaging Methods for Palaeoecology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-vegan >= 2.2.0
BuildRequires:    R-CRAN-princurve >= 2.0.2
BuildRequires:    R-mgcv 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-brglm 
BuildRequires:    R-lattice 
Requires:         R-CRAN-vegan >= 2.2.0
Requires:         R-CRAN-princurve >= 2.0.2
Requires:         R-mgcv 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-brglm 
Requires:         R-lattice 

%description
Fits Modern Analogue Technique and Weighted Averaging transfer function
models for prediction of environmental data from species data, and related
methods used in palaeoecology.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
