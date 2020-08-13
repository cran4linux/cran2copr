%global packname  vtreat
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Statistically Sound 'data.frame' Processor/Conditioner

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-wrapr >= 2.0.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-wrapr >= 2.0.0
Requires:         R-stats 
Requires:         R-CRAN-digest 

%description
A 'data.frame' processor/conditioner that prepares real-world data for
predictive modeling in a statistically sound manner. 'vtreat' prepares
variables so that data has fewer exceptional cases, making it easier to
safely use models in production. Common problems 'vtreat' defends against:
'Inf', 'NA', too many categorical levels, rare categorical levels, and new
categorical levels (levels seen during application, but not during
training). Reference: "'vtreat': a data.frame Processor for Predictive
Modeling", Zumel, Mount, 2016, <DOI:10.5281/zenodo.1173313>.

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
