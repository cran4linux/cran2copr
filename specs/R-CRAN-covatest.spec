%global packname  covatest
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          2%{?dist}%{?buildtag}
Summary:          Tests on Properties of Space-Time Covariance Functions

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spacetime >= 1.0.0
BuildRequires:    R-CRAN-sp >= 0.9.72
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-gstat 
Requires:         R-CRAN-spacetime >= 1.0.0
Requires:         R-CRAN-sp >= 0.9.72
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-gstat 

%description
Tests on properties of space-time covariance functions. Tests on symmetry,
separability and for assessing different forms of non-separability are
available. Moreover tests on some classes of covariance functions, such
that the classes of product-sum models, Gneiting models and integrated
product models have been provided.  It is the companion R package to the
papers of Cappello, C., De Iaco, S., Posa, D., 2018, Testing the type of
non-separability and some classes of space-time covariance function models
<doi:10.1007/s00477-017-1472-2> and Cappello, C., De Iaco, S., Posa, D.,
2020, covatest: an R package for selecting a class of space-time
covariance functions <doi:10.18637/jss.v094.i01>.

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
