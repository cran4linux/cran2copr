%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  visual.kaito
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive 3D Visualizations for Group Comparisons

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Draws interactive, rotatable statistical visualizations in three
dimensions, built on 'plotly'. Two families of plots are provided.
Triaxial box plots (boxplot3d(), boxplot3d_interactive()) compare groups
on three continuous variables at once, with Tukey, fixed-percentile, mean
+/- SD, and letter-value box/whisker conventions, plus parametric and
non-parametric significance testing (per-axis and joint 3D via MANOVA /
PERMANOVA). Bivariate density plots (ttest_plot3d(), manova_plot3d())
compare two or more groups on two continuous variables as overlapping 3D
density surfaces, reporting per-axis t-tests together with a joint
Hotelling's T-squared test (two groups), or a one-way MANOVA omnibus test
with Bonferroni, Tukey, Fisher's LSD, and Dunnett post-hoc comparisons
(more than two groups). All plots include live, pre-computed controls
(view, method, scale, transparency) so results can be explored
interactively without re-running R code.

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
