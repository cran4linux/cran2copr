%global packname  maditr
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          Fast Data Aggregation, Modification, and Filtering with Pipesand 'data.table'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.11
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-data.table >= 1.11

%description
Package provides pipe-style interface for 'data.table'. It preserves all
'data.table' features without significant impact on performance. 'let' and
'take' functions are simplified interfaces for most common data
manipulation tasks. For example, you can write 'mtcars %>% take(mean(mpg),
by = am)' for aggregation or 'mtcars %>% let(hp_wt = hp/wt, hp_wt_mpg =
hp_wt/mpg)' for modification. Use 'take_if/let_if' for conditional
aggregation/modification. 'query_if' function translates its arguments
one-to-one to '[.data.table' method. Additionally there are some
conveniences such as automatic 'data.frame' conversion to 'data.table'.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
