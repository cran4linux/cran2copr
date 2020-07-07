%global packname  Rdistance
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          3%{?dist}
Summary:          Distance-Sampling Analyses for Density and Abundance Estimation

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Distance-sampling is a popular method for estimating density and abundance
of organisms in ecology. Rdistance contains routines that assist with
analysis of distance-sampling data collected on point or line transects.
Distance models are specified using regression-like formula (similar to
lm, glm, etc.). Abundance routines perform automated bootstrapping and
automated detection-function selection. Overall (study area) and
site-level (transect or point) abundance estimates are available. A large
suite of classical, parametric detection functions are included along with
some uncommon parametric functions (e.g., Gamma, negative exponential) and
non-parametric smoothed distance functions. Custom (user-defined)
detection functions are easily implemented (see vignette). The help files
and vignettes have been vetted by multiple authors and tested in workshop
settings.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
