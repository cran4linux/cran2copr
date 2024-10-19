%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ODT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Decision Trees Algorithm

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-DiagrammeRsvg 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-rsvg 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-data.tree 
Requires:         R-stats 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-DiagrammeRsvg 
Requires:         R-grDevices 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-rsvg 

%description
Implements a tree-based method specifically designed for personalized
medicine applications. By using genomic and mutational data, 'ODT'
efficiently identifies optimal drug recommendations tailored to individual
patient profiles. The 'ODT' algorithm constructs decision trees that
bifurcate at each node, selecting the most relevant markers (discrete or
continuous) and corresponding treatments, thus ensuring that
recommendations are both personalized and statistically robust. This
iterative approach enhances therapeutic decision-making by refining
treatment suggestions until a predefined group size is achieved. Moreover,
the simplicity and interpretability of the resulting trees make the method
accessible to healthcare professionals. Includes functions for training
the decision tree, making predictions on new samples or patients, and
visualizing the resulting tree. For detailed insights into the
methodology, please refer to Gimeno et al. (2023)
<doi:10.1093/bib/bbad200>.

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
