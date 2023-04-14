%global __brp_check_rpaths %{nil}
%global packname  madness
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          3%{?dist}%{?buildtag}
Summary:          Automatic Differentiation of Multivariate Operations

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-methods 
Requires:         R-Matrix 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-expm 
Requires:         R-methods 

%description
An object that supports automatic differentiation of matrix- and
multidimensional-valued functions with respect to multidimensional
independent variables. Automatic differentiation is via 'forward
accumulation'.

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
%{rlibdir}/%{packname}
