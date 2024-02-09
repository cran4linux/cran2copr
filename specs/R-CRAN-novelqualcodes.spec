%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  novelqualcodes
%global packver   0.13.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualise the Path to a Stopping Point in Qualitative Interviews Based on Novel Codes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-naturalsort 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpattern 
BuildRequires:    R-utils 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-naturalsort 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpattern 
Requires:         R-utils 

%description
In semi-structured interviews that use the 'framework' method, it is not
always clear how refinements to interview questions affect the decision of
when to stop interviews. The trend of 'novel' and 'duplicate' interview
codes (novel codes are information that other interviewees have not
previously mentioned) provides insight into the richness of qualitative
information. This package provides tools to visualise when refinements
occur and how that affects the trends of novel and duplicate codes. These
visualisations, when used progressively as new interviews are finished,
can help the researcher to decide on a stopping point for their
interviews.

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
