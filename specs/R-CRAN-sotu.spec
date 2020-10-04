%global packname  sotu
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          United States Presidential State of the Union Addresses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
The President of the United States is constitutionally obligated to
provide a report known as the 'State of the Union'. The report summarizes
the current challenges facing the country and the president's upcoming
legislative agenda. While historically the State of the Union was often a
written document, in recent decades it has always taken the form of an
oral address to a joint session of the United States Congress. This
package provides the raw text from every such address with the intention
of being used for meaningful examples of text analysis in R. The corpus is
well suited to the task as it is historically important, includes material
intended to be read and material intended to be spoken, and it falls in
the public domain. As the corpus spans over two centuries it is also a
good test of how well various methods hold up to the idiosyncrasies of
historical texts. Associated data about each address, such as the year,
president, party, and format, are also included.

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
%{rlibdir}/%{packname}/INDEX
