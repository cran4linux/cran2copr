%global __brp_check_rpaths %{nil}
%global packname  Rwordseg
%global packver   0.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Chinese Word Segmentation

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tmcn 
BuildRequires:    R-CRAN-HMM 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-tmcn 
Requires:         R-CRAN-HMM 

%description
Provides interfaces and useful tools for Chinese word segmentation.
Implements a segmentation algorithm based on Hidden Markov Model (HMM) in
native R codes. Methods for HHMM-Based Chinese lexical analyzer are as
described in : Hua-Ping Zhang et al., (2003)
<doi:10.3115/1119250.1119280>.

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
%doc %{rlibdir}/%{packname}/models
%{rlibdir}/%{packname}/INDEX
