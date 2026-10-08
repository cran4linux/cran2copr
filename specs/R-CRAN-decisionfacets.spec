%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  decisionfacets
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Decision Accuracy and Consistency for Rater-Mediated Exams

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Answers "would this candidate have passed with a different set of raters?"
for rater-mediated exams such as oral examinations, objective structured
clinical examinations and essay scoring. Builds on the many-facet
extension of the rating scale model (Andrich, 1978,
<doi:10.1007/BF02293814>) to compute counterfactual pass probabilities
under the observed, an average-severity and a random rater panel, under an
explicit decision rule (raw total, fair average or measure), and splits
expected misclassification into measurement error and rater assignment,
extending item response theory classification accuracy (Lee, 2010,
<doi:10.1111/j.1745-3984.2009.00096.x>) to rater effects. Models can be
fitted with 'TAM' or a built-in joint maximum likelihood estimator.

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
