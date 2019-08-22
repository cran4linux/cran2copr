%global packname  blastula
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Easily Send HTML Email Messages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-commonmark >= 1.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-glue >= 1.2.0
BuildRequires:    R-CRAN-tidyr >= 0.8.0
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-CRAN-downloader >= 0.4
BuildRequires:    R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-commonmark >= 1.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-glue >= 1.2.0
Requires:         R-CRAN-tidyr >= 0.8.0
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-CRAN-downloader >= 0.4
Requires:         R-CRAN-htmltools >= 0.3.6

%description
Compose and send out responsive HTML email messages that render perfectly
across a range of email clients and device sizes. Messages are composed
using 'Markdown' and a text interpolation system that allows for the
injection of evaluated R code within the message body, footer, and subject
line. Helper functions let the user insert embedded images, web link
buttons, and 'ggplot2' plot objects into the message body. Messages can be
sent through an 'SMTP' server or through the 'Mailgun' API service
<http://mailgun.com/>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/INDEX
