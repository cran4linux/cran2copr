%global __brp_check_rpaths %{nil}
%global packname  LilRhino
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          For Implementation of Feed Reduction, Learning Examples, NLP andCode Management

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-beepr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-textclean 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-neuralnet 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-beepr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-parallel 
Requires:         R-CRAN-textclean 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-neuralnet 

%description
This is for code management functions, NLP tools, a Monty Hall simulator,
and for implementing my own variable reduction technique called Feed
Reduction
<http://wbbpredictions.com/wp-content/uploads/2018/12/Redditbot_Paper.pdf>.
The Feed Reduction technique is not yet published, but is merely a tool
for implementing a series of binary neural networks meant for reducing
data into N dimensions, where N is the number of possible values of the
response variable.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
