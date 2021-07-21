%global __brp_check_rpaths %{nil}
%global packname  KHQ
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Calculating 'KHQ' Scores and 'KHQ5D' Utility Index Scores

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-openxlsx 
Requires:         R-stats 

%description
The King's Health Questionnaire (KHQ) is a disease-specific,
self-administered questionnaire designed specific to assess the impact of
Urinary Incontinence (UI) on Quality of Life. The questionnaire was
developed by Kelleher and collaborators (1997)
<doi:10.1111/j.1471-0528.1997.tb11006.x>. It is a simple, acceptable and
reliable measure to use in the clinical setting and a research tool that
is useful in evaluating UI treatment outcomes. The KHQ five dimensions
(KHQ5D) is a condition-specific preference-based measure developed by
Brazier and collaborators (2008) <doi:10.1177/0272989X07301820>. Although
not as popular as the SF6D <doi:10.1016/S0895-4356(98)00103-6> and EQ-5D
<https://euroqol.org/>, the KHQ5D measures health-related quality of life
(HRQoL) specifically for UI, not general conditions like the others two
instruments mentioned. The KHQ5D ca be used in the clinical and economic
evaluation of health care. The subject self-rates their health in terms of
five dimensions: Role Limitation (RL), Physical Limitations (PL), Social
Limitations (SL), Emotions (E), and Sleep (S). Frequently the scores on
these five dimensions are converted to a single utility index using
country specific value sets, which can be used in the clinical and
economic evaluation of health care as well as in population health
surveys. This package provides methods to calculate scores for each
dimension of the KHQ; converts KHQ item scores to KHQ5D scores; and also
calculates the utility index of the KHQ5D.

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
