%global packname  permimp
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Conditional Permutation Importance

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest >= 4.6.14
BuildRequires:    R-survival >= 2.44.1.1
BuildRequires:    R-CRAN-party >= 1.3.3
BuildRequires:    R-CRAN-ipred >= 0.9.6
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-randomForest >= 4.6.14
Requires:         R-survival >= 2.44.1.1
Requires:         R-CRAN-party >= 1.3.3
Requires:         R-CRAN-ipred >= 0.9.6
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
An add-on to the 'party' package, with a faster implementation of the
partial-conditional permutation importance for random forests. The
standard permutation importance is implemented exactly the same as in the
'party' package. The conditional permutation importance can be computed
faster, with an option to be backward compatible to the 'party'
implementation. The package is compatible with random forests fit using
the 'party' and the 'randomForest' package. The methods are described in
Strobl et al. (2007) <doi:10.1186/1471-2105-8-25> and Debeer and Strobl
(2020).

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
