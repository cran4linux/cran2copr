%global packname  nlist
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Lists of Numeric Atomic Objects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-term >= 0.2.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-universals 
BuildRequires:    R-CRAN-extras 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-term >= 0.2.0
Requires:         R-stats 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-universals 
Requires:         R-CRAN-extras 
Requires:         R-CRAN-lifecycle 

%description
Create and manipulate numeric list ('nlist') objects. An 'nlist' is an S3
list of uniquely named numeric objects. An numeric object is an integer or
double vector, matrix or array. An 'nlists' object is a S3 class list of
'nlist' objects with the same names, dimensionalities and typeofs.
Numeric list objects are of interest because they are the raw data inputs
for analytic engines such as 'JAGS', 'STAN' and 'TMB'.  Numeric lists
objects, which are useful for storing multiple realizations of of
simulated data sets, can be converted to coda::mcmc and coda::mcmc.list
objects.

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
