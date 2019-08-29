%global packname  m2b
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Movement to Behaviour Inference using Random Forest

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-caret 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Prediction of behaviour from movement characteristics using observation
and random forest for the analyses of movement data in ecology. From
movement information (speed, bearing...) the model predicts the observed
behaviour (movement, foraging...) using random forest. The model can then
extrapolate behavioural information to movement data without direct
observation of behaviours. The specificity of this method relies on the
derivation of multiple predictor variables from the movement data over a
range of temporal windows. This procedure allows to capture as much
information as possible on the changes and variations of movement and
ensures the use of the random forest algorithm to its best capacity. The
method is very generic, applicable to any set of data providing movement
data together with observation of behaviour.

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
%{rlibdir}/%{packname}/INDEX
