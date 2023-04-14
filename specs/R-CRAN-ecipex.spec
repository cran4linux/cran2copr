%global __brp_check_rpaths %{nil}
%global packname  ecipex
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Efficient Calculation of Fine Structure Isotope Patterns viaFourier Transforms of Simplex-Based Elemental Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CHNOSZ 
Requires:         R-CRAN-CHNOSZ 

%description
Provides a function that quickly computes the fine structure isotope
patterns of a set of chemical formulas to a given degree of accuracy (up
to the limit set by errors in floating point arithmetic). A data-set
comprising the masses and isotopic abundances of individual elements is
also provided and calculation of isotopic gross structures is also
supported.

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
