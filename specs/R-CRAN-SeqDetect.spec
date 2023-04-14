%global __brp_check_rpaths %{nil}
%global packname  SeqDetect
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          3%{?dist}%{?buildtag}
Summary:          Sequence and Latent Process Detector

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-eventdataR 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-eventdataR 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 

%description
Sequence detector in this package contains a specific automaton model that
can be used to learn and detect data and process sequences. Automaton
model in this package is capable of learning and tracing sequences.
Automaton model can be found in Krleža, Vrdoljak, Brčić (2019)
<doi:10.1109/ACCESS.2019.2955245>. This research has been partly supported
under Competitiveness and Cohesion Operational Programme from the European
Regional and Development Fund, as part of the Integrated Anti-Fraud System
project no. KK.01.2.1.01.0041. This research has also been partly
supported by the European Regional Development Fund under the grant
KK.01.1.1.01.0009.

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
%{rlibdir}/%{packname}
