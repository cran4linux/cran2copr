%global packname  blastula
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          2%{?dist}
Summary:          Easily Send HTML Email Messages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3
BuildRequires:    R-CRAN-commonmark >= 1.7
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-fs >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-mime >= 0.6
BuildRequires:    R-CRAN-rlang >= 0.4.1
BuildRequires:    R-CRAN-htmltools >= 0.4.0
BuildRequires:    R-CRAN-getPass >= 0.2.2
BuildRequires:    R-CRAN-base64enc >= 0.1.3
BuildRequires:    R-CRAN-uuid >= 0.1.2
BuildRequires:    R-CRAN-here >= 0.1
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-curl >= 4.3
Requires:         R-CRAN-commonmark >= 1.7
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-fs >= 1.3.1
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-mime >= 0.6
Requires:         R-CRAN-rlang >= 0.4.1
Requires:         R-CRAN-htmltools >= 0.4.0
Requires:         R-CRAN-getPass >= 0.2.2
Requires:         R-CRAN-base64enc >= 0.1.3
Requires:         R-CRAN-uuid >= 0.1.2
Requires:         R-CRAN-here >= 0.1
Requires:         R-CRAN-digest 
Requires:         R-CRAN-rmarkdown 

%description
Compose and send out responsive HTML email messages that render perfectly
across a range of email clients and device sizes. Helper functions let the
user insert embedded images, web link buttons, and 'ggplot2' plot objects
into the message body. Messages can be sent through an 'SMTP' server,
through the 'RStudio Connect' service, or through the 'Mailgun' API
service <http://mailgun.com/>.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/cerberus-meta.html
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example_files
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/rmd
%doc %{rlibdir}/%{packname}/social_icons
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
