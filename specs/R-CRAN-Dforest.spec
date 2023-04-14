%global __brp_check_rpaths %{nil}
%global packname  Dforest
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          3%{?dist}%{?buildtag}
Summary:          Decision Forest

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-rpart 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-stats 

%description
Provides R-implementation of Decision forest algorithm, which combines the
predictions of multiple independent decision tree models for a consensus
decision. In particular, Decision Forest is a novel pattern-recognition
method which can be used to analyze: (1) DNA microarray data; (2)
Surface-Enhanced Laser Desorption/Ionization Time-of-Flight Mass
Spectrometry (SELDI-TOF-MS) data; and (3) Structure-Activity Relation
(SAR) data. In this package, three fundamental functions are provided, as
(1)DF_train, (2)DF_pred, and (3)DF_CV. run Dforest() to see more
instructions. Weida Tong (2003) <doi:10.1021/ci020058s>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
