%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NeuroDataSets
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Comprehensive Collection of Neuroscience and Brain-Related Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Offers a rich and diverse collection of datasets focused on the brain,
nervous system, and related disorders. The package includes clinical,
experimental, neuroimaging, behavioral, cognitive, and simulated data on
conditions such as Parkinson's disease, Alzheimer's disease, dementia,
epilepsy, schizophrenia, autism spectrum disorder, attention deficit,
hyperactivity disorder, Tourette's syndrome, traumatic brain injury,
gliomas, migraines, headaches, sleep disorders, concussions, encephalitis,
subarachnoid hemorrhage, and mental health conditions. Datasets cover
structural and functional brain data, cross-sectional and longitudinal MRI
imaging studies, neurotransmission, gene expression, cognitive
performance, intelligence metrics, sleep deprivation effects, treatment
outcomes, brain-body relationships across species, neurological injury
patterns, and acupuncture interventions. Data sources include
peer-reviewed studies, clinical trials, military health records, sports
injury databases, and international comparative studies. Designed for
researchers, neuroscientists, clinicians, psychologists, data scientists,
and students, this package facilitates exploratory data analysis,
statistical modeling, and hypothesis testing in neuroscience and
neuroepidemiology.

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
