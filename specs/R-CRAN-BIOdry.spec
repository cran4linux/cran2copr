%global __brp_check_rpaths %{nil}
%global packname  BIOdry
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Multilevel Modeling of Dendroclimatical Fluctuations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-ecodist 
Requires:         R-nlme 
Requires:         R-CRAN-ecodist 

%description
Multilevel ecological data series (MEDS) are sequences of observations
ordered according to temporal/spatial hierarchies that are defined by
sample designs, with sample variability confined to ecological factors.
Dendroclimatic MEDS of tree rings and climate are modeled into normalized
fluctuations of tree growth and aridity.  Modeled fluctuations (model
frames) are compared with Mantel correlograms on multiple levels defined
by sample design. Package implementation can be understood by running
examples in modelFrame(), and muleMan() functions.

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
