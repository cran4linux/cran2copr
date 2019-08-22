%global packname  text2speech
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          Text to Speech

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mscstts >= 0.5.1
BuildRequires:    R-CRAN-aws.polly 
BuildRequires:    R-CRAN-aws.signature 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-googleAuthR 
BuildRequires:    R-CRAN-googleLanguageR 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-mscstts >= 0.5.1
Requires:         R-CRAN-aws.polly 
Requires:         R-CRAN-aws.signature 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-googleAuthR 
Requires:         R-CRAN-googleLanguageR 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-magrittr 

%description
Unifies different text to speech engines, such as Google, Microsoft, and
Amazon.  Text synthesis can be done in any engine with a simple switch of
an argument denoting the service requested.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
