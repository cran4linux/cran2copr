%global packname  asymmetry.measures
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Asymmetry Measures for Probability Density Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-skewt 
BuildRequires:    R-CRAN-gamlss.dist 
Requires:         R-stats 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-skewt 
Requires:         R-CRAN-gamlss.dist 

%description
Provides functions and examples for the weak and strong density asymmetry
measures in the articles: "A measure of asymmetry", Patil, Patil and
Bagkavos (2012) <doi:10.1007/s00362-011-0401-6> and "A measure of
asymmetry based on a new necessary and sufficient condition for symmetry",
Patil, Bagkavos and Wood (2014) <doi:10.1007/s13171-013-0034-z>. The
measures provided here are useful for quantifying the asymmetry of the
shape of a density of a random variable. The package facilitates
implementation of the measures which are applicable in a variety of fields
including e.g. probability theory, statistics and economics.

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
