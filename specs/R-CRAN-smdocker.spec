%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smdocker
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Build 'Docker Images' in 'Amazon SageMaker Studio' using 'Amazon Web Service CodeBuild'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-paws.compute 
BuildRequires:    R-CRAN-paws.developer.tools 
BuildRequires:    R-CRAN-paws.machine.learning 
BuildRequires:    R-CRAN-paws.management 
BuildRequires:    R-CRAN-paws.storage 
BuildRequires:    R-CRAN-paws.security.identity 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-paws.compute 
Requires:         R-CRAN-paws.developer.tools 
Requires:         R-CRAN-paws.machine.learning 
Requires:         R-CRAN-paws.management 
Requires:         R-CRAN-paws.storage 
Requires:         R-CRAN-paws.security.identity 
Requires:         R-CRAN-zip 
Requires:         R-stats 
Requires:         R-utils 

%description
Allows users to easily build custom 'docker images'
<https://docs.docker.com/> from 'Amazon Web Service Sagemaker'
<https://aws.amazon.com/sagemaker/> using 'Amazon Web Service CodeBuild'
<https://aws.amazon.com/codebuild/>.

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
