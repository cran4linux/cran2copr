%global __brp_check_rpaths %{nil}
%global packname  rngSetSeed
%global packver   0.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Seeding the Default RNG with a Numeric Vector

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
A function setVectorSeed() is provided. Its argument is a numeric vector
of an arbitrary nonzero length, whose components have integer values from
[0, 2^32-1]. The input vector is transformed using AES (Advanced
Encryption Standard) algorithm into an initial state of Mersenne-Twister
random number generator. The function provides a better alternative to the
R base function set.seed(), if the input vector is a single integer.
Initializing a stream of random numbers with a vector is a convenient way
to obtain several streams, each of which is identified by several integer
indices.

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
