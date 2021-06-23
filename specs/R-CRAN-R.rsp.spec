%global __brp_check_rpaths %{nil}
%global packname  R.rsp
%global packver   0.44.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.44.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Generation of Scientific Reports

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.methodsS3 >= 1.7.1
BuildRequires:    R-CRAN-R.oo >= 1.23.0
BuildRequires:    R-CRAN-digest >= 0.6.13
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-R.cache 
Requires:         R-CRAN-R.methodsS3 >= 1.7.1
Requires:         R-CRAN-R.oo >= 1.23.0
Requires:         R-CRAN-digest >= 0.6.13
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-R.cache 

%description
The RSP markup language makes any text-based document come alive.  RSP
provides a powerful markup for controlling the content and output of
LaTeX, HTML, Markdown, AsciiDoc, Sweave and knitr documents (and more),
e.g. 'Today's date is <%=Sys.Date()%>'.  Contrary to many other literate
programming languages, with RSP it is straightforward to loop over
mixtures of code and text sections, e.g. in month-by-month summaries.  RSP
has also several preprocessing directives for incorporating static and
dynamic contents of external files (local or online) among other things.
Functions rstring() and rcat() make it easy to process RSP strings,
rsource() sources an RSP file as it was an R script, while rfile()
compiles it (even online) into its final output format, e.g.
rfile('report.tex.rsp') generates 'report.pdf' and rfile('report.md.rsp')
generates 'report.html'.  RSP is ideal for self-contained scientific
reports and R package vignettes.  It's easy to use - if you know how to
write an R script, you'll be up and running within minutes.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
