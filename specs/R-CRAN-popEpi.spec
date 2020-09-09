%global packname  popEpi
%global packver   0.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.8
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Epidemiological Analysis using Population Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Epi >= 2.0
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-survival 
Requires:         R-CRAN-Epi >= 2.0
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-survival 

%description
Enables computation of epidemiological statistics, including those where
counts or mortality rates of the reference population are used. Currently
supported: excess hazard models, rates, mean survival times, relative
survival, and standardized incidence and mortality ratios (SIRs/SMRs), all
of which can be easily adjusted for by covariates such as age. Fast
splitting and aggregation of 'Lexis' objects (from package 'Epi') and
other computations achieved using 'data.table'.

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
