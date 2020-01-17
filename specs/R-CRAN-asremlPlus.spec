%global packname  asremlPlus
%global packver   4.1-36
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.36
Release:          1%{?dist}
Summary:          Augments 'ASReml-R' in Fitting Mixed Models and PackagesGenerally in Exploring Prediction Differences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dae 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-dae 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grDevices 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Assists in automating the testing of terms in mixed models when 'asreml'
is used to fit the models. Also used to display, in tables and graphs,
predictions obtained using any model fitting function and to explore
differences between predictions. The content falls into the following
natural groupings: (i) Data, (ii) Object manipulation functions, (iii)
Model modification functions, (iv) Model testing functions, (v) Model
diagnostics functions, (vi) Prediction production and presentation
functions, (vii) Response transformation functions, and (viii)
Miscellaneous functions. A history of the fitting of a sequence of models
is kept in a data frame. Procedures are available for choosing models that
conform to the hierarchy or marginality principle and for displaying
predictions for significant terms in tables and graphs. The 'asreml'
package provides a computationally efficient algorithm for fitting mixed
models using Residual Maximum Likelihood. It is a commercial packages that
can be purchased from 'VSNi' <http://www.vsni.co.uk/> as 'asreml-R', who
will supply a zip file for local installation/updating. It is not needed
for functions that are methods for 'alldiffs' and 'data.frame' objects.
The package 'asremPlus' can also be installed from
<http://chris.brien.name/rpackages/>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
