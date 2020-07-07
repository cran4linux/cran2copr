%global packname  seqhandbook
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Miscellaneous Tools for Sequence Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-TraMineR 
Requires:         R-CRAN-TraMineR 

%description
It provides miscellaneous sequence analysis functions for describing
episodes in individual sequences, measuring association between domains in
multidimensional sequence analysis (see Piccarreta (2017)
<doi:10.1177/0049124115591013>), heat maps of sequence data, Globally
Interdependent Multidimensional Sequence Analysis (see Robette et al
(2015) <doi:10.1177/0081175015570976>), smoothing sequences for index
plots (see Piccarreta (2012) <doi:10.1177/0049124112452394>), coding
sequences for Qualitative Harmonic Analysis (see Deville (1982)),
measuring stress from multidimensional scaling factors (see Piccarreta and
Lior (2010) <doi:10.1111/j.1467-985X.2009.00606.x>), symmetrical (or
canonical) Partial Least Squares (see Bry (1996)).

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
