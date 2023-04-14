%global __brp_check_rpaths %{nil}
%global packname  needmining
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Simple Needmining Implementation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rtweet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-tau 
BuildRequires:    R-CRAN-tm 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-rtweet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-tau 
Requires:         R-CRAN-tm 

%description
Showcasing needmining (the semi-automatic extraction of customer needs
from social media data) with Twitter data. It uses the handling of the
Twitter API provided by the package 'rtweet' and the textmining algorithms
provided by the package 'tm'. Niklas Kuehl (2016)
<doi:10.1007/978-3-319-32689-4_14> wrote an introduction to the topic of
needmining.

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
