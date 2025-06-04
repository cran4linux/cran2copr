%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DigestiveDataSets
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Curated Collection of Digestive System and Gastrointestinal Disease Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Provides an extensive and curated collection of datasets related to the
digestive system, stomach, intestines, liver, pancreas, and associated
diseases. This package includes clinical trials, observational studies,
experimental datasets, cohort data, and case series involving
gastrointestinal disorders such as gastritis, ulcers, pancreatitis, liver
cirrhosis, colon cancer, colorectal conditions, Helicobacter pylori
infection, irritable bowel syndrome, intestinal infections, and
post-surgical outcomes. The datasets support educational, clinical, and
research applications in gastroenterology, public health, epidemiology,
and biomedical sciences. Designed for researchers, clinicians, data
scientists, students, and educators interested in digestive diseases, the
package facilitates reproducible analysis, modeling, and hypothesis
testing using real-world and historical data.

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
