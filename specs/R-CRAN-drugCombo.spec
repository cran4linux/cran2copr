%global packname  drugCombo
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          Drug Interaction Modeling Based on Loewe Additivity FollowingHarbron's Approach

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-BIGL >= 0.9
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-BIGL >= 0.9
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-rgl 
Requires:         R-nlme 
Requires:         R-CRAN-Deriv 
Requires:         R-methods 
Requires:         R-stats 

%description
Perform assessment of synergy/antagonism for drug combinations based on
the Loewe additivity model, following Harbron's approach (Statistics in
Medicine, 2010, <doi:10.1002/sim.3916>). The package allows flexible
modeling of the drug interaction index and supports "2-stage" estimation
in addition to "1-stage" estimation, including bootstrap-based confidence
intervals. The method requires data on the monotherapy responses and the
package accommodates both checkerboard and ray designs. Functions are
available for graphical exploration of model goodness-of-fit and
diagnostics, as well as for synergy/antagonism assessment in 2D and 3D.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
