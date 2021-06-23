%global __brp_check_rpaths %{nil}
%global packname  BayesianPower
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          2%{?dist}%{?buildtag}
Summary:          Sample Size and Power for Comparing Inequality ConstrainedHypotheses

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A collection of methods to determine the required sample size for the
evaluation of inequality constrained hypotheses by means of a Bayes
factor. Alternatively, for a given sample size, the unconditional error
probabilities or the expected conditional error probabilities can be
determined. Additional material on the methods in this package is
available in Klaassen, F., Hoijtink, H. & Gu, X. (2019)
<doi:10.31219/osf.io/d5kf3>.

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

%files
%{rlibdir}/%{packname}
