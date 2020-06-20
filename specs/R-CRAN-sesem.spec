%global packname  sesem
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Spatially Explicit Structural Equation Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-gplots 
Requires:         R-CRAN-lavaan 
Requires:         R-mgcv 
Requires:         R-CRAN-gplots 

%description
Structural equation modeling is a powerful statistical approach for the
testing of networks of direct and indirect theoretical causal
relationships in complex data sets with inter-correlated dependent and
independent variables. Here we implement a simple method for spatially
explicit structural equation modeling based on the analysis of variance
co-variance matrices calculated across a range of lag distances. This
method provides readily interpreted plots of the change in path
coefficients across scale.

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
