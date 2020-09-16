%global packname  DJL
%global packver   3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Distance Measure Based Judgment and Learning

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-lpSolveAPI 
Requires:         R-CRAN-car 
Requires:         R-CRAN-lpSolveAPI 

%description
Implements various decision support tools related to the Econometrics &
Technometrics. Subroutines include correlation reliability test,
Mahalanobis distance measure for outlier detection, combinatorial search
(all possible subset regression), non-parametric efficiency analysis
measures: DDF (directional distance function), DEA (data envelopment
analysis), HDF (hyperbolic distance function), SBM (slack-based measure),
and SF (shortage function), benchmarking, Malmquist productivity analysis,
risk analysis, technology adoption model, new product target setting, etc.

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
