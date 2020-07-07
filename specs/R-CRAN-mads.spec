%global packname  mads
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}
Summary:          Multi-Analysis Distance Sampling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mrds 
BuildRequires:    R-stats 
Requires:         R-CRAN-mrds 
Requires:         R-stats 

%description
Performs distance sampling analyses on a number of species at once and can
account for unidentified sightings, model uncertainty and covariate
uncertainty. Unidentified sightings refer to sightings which cannot be
allocated to a single species but may instead be allocated to a group of
species. The abundance of each unidentified group is estimated and then
prorated to the species estimates. Model uncertainty should be
incorporated when multiple models give equally good fit to the data but
lead to large differences in estimated density / abundance. Covariate
uncertainty should be incorporated when covariates cannot be measured
accurately, for example this is often the case for group size in marine
mammal surveys. Variance estimation for these methods is via a non
parametric bootstrap. The methods implemented are described in Gerodette
T. and Forcada J. (2005) <doi:10.3354/meps291001> Non-recovery of two
spotted and spinner dolphin populations in the eastern tropical Pacific
Ocean.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/testData
%{rlibdir}/%{packname}/INDEX
