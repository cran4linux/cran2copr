%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  exactcond
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exact Conditional Reference Distributions for Tables and Selected Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Reference distributions that are exact at every sample size, obtained by
conditioning on a statistic sufficient for the nuisance parameter rather
than by appealing to an asymptotic approximation. Two forms of
conditioning are supplied. For a two-way table the row and column totals
are sufficient for the marginal parameters, so conditioning on both
margins leaves the Fisher-Yates law, sampled here exactly by random
permutation of the column labels; statistics include Goodman's
linear-by-linear association and, for nominal rows against an ordinal
column, the dispersion of the row mean scores, whose components are the
group contrasts themselves. A two-table form conditions further on the
total score to cancel a common association parameter, giving a
nuisance-free test that two tables share it. For a linear model under a
null in which the tested structure is absent, a statistic invariant to the
coefficients and the error scale depends on the data only through the
residual direction, which is uniform on the sphere of the residual space;
the reference stays exact when the statistic is maximised over candidate
structures, and so remains valid after a spatial weight matrix has been
chosen by fit. Every replicate draws from its own stream, so results do
not depend on the thread count. The same C sources back the 'Python'
package 'exactcond'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
